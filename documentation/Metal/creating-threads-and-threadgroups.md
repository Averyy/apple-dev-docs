# Creating threads and threadgroups

**Framework**: Metal

Learn how Metal organizes compute-processing workloads.

#### Overview

Recall from [`Processing a texture in a compute function`](processing-a-texture-in-a-compute-function.md) that when you dispatch your compute pass, Metal executes your kernel function over a 1D, 2D, or 3D grid. Each point in the grid represents a single instance of your kernel function, referred to as a . For example, in image processing, the grid is typically a 2D matrix of threads—representing the entire image—with each thread corresponding to a single pixel of the image being processed.

Threads are organized into  that are executed together and can share a common block of memory. While sometimes kernel functions are designed so that threads run independently of each other, it’s also common for threads in a threadgroup to collaborate on their working set.

##### Identification of Threads By Position in Grid

[`Figure 1`](compute_passes/creating_threads_and_threadgroups#2928936.md) shows how an image being processed by a compute kernel is divided into threadgroups and how each threadgroup is composed of individual threads. Each thread processes a single pixel.

![A grid divided into threadgroups that are composed of individual threads.](https://docs-assets.developer.apple.com/published/968ef737b344f13ae030c348b9ec2267/media-2928936%402x.png)

A thread can be identified by its position in the grid; it’s this unique position that allows your kernel function to do something different for each thread. The sample kernel function in [`Processing a texture in a compute function`](processing-a-texture-in-a-compute-function.md), below, shows how a thread’s position in the grid is passed into the function as a parameter. In this case, the parameter, `gid`, is a vector representing 2D coordinates and is used to both read from and write to a particular location in a texture.

```metal
kernel void
grayscaleKernel(texture2d<half, access::read>  inTexture  [[texture(AAPLTextureIndexInput)]],
                texture2d<half, access::write> outTexture [[texture(AAPLTextureIndexOutput)]],
                uint2                          gid        [[thread_position_in_grid]])
{
    if((gid.x >= outTexture.get_width()) || (gid.y >= outTexture.get_height()))
    {
        return;
    }
    half4 inColor  = inTexture.read(gid);
    half  gray     = dot(inColor.rgb, kRec709Luma);
    outTexture.write(half4(gray, gray, gray, 1.0), gid);
}
```

`[[thread_position_in_grid]]` is an . Attribute qualifiers, identifiable by their double square-bracket syntax, allow kernel parameters to be bound to resources and built-in variables, in this case the thread’s position in the grid to the kernel function.

For example, given a grid of 16 x 16 threads partitioned into 2 x 4 threadgroups of 8 x 4 threads, a single thread (shown in [`Figure 2`](compute_passes/creating_threads_and_threadgroups#2929009.md) in red) has a position in the grid of (9,10):

![The position of a single thread in a 16 x 16 grid.](https://docs-assets.developer.apple.com/published/f81f3847d494742e2d253658ddbe8804/media-2929009%402x.png)

##### Identification of Threads By Position in Threadgroup

A thread’s position in its threadgroup is also available as the attribute qualifier `[[thread_position_in_threadgroup]]`, and a threadgroup’s position in the grid is available as `[[threadgroup_position_in_grid]]`.

Depending on the shape of the grid, these position attributes are either a scalar value, or a two- or three-element vector. In the case of a 2D grid, position attributes are two-element vectors, with the origin at the top-left.

The thread identified in [`Figure 2`](compute_passes/creating_threads_and_threadgroups#2929009.md) is in the threadgroup with a position in the grid of (1,2), and its position in that threadgroup is (1,2), as shown in [`Figure 3`](compute_passes/creating_threads_and_threadgroups#2929421.md):

![The position of a single thread in a threadgroup.](https://docs-assets.developer.apple.com/published/c931c075f557ee6b7e5fae31270cde1f/media-2929421%402x.png)

Using the following code, you can also calculate a thread’s position in the grid based on its position in its threadgroup and that threadgroup’s size and position in the grid:

```metal
kernel void 
myKernel(uint2 threadgroup_position_in_grid   [[ threadgroup_position_in_grid ]],
         uint2 thread_position_in_threadgroup [[ thread_position_in_threadgroup ]],
         uint2 threads_per_threadgroup        [[ threads_per_threadgroup ]]) 
{
    
    uint2 thread_position_in_grid = 
        (threadgroup_position_in_grid * threads_per_threadgroup) + 
        thread_position_in_threadgroup;
}
```

##### Simd Groups

The threads in a threadgroup are further organized into single-instruction, multiple-data (SIMD) groups, also known as  or , that execute concurrently. The threads in a SIMD group execute the same code. Avoid writing code that could cause your kernel function to ; that is, to follow different code paths. A typical example of divergence is caused by using an  statement. Even if a single thread in a SIMD group takes a different path from the others, all threads in that group execute both branches, and the execution time for the group is the sum of the execution time of both branches.

The division of threadgroups into SIMD groups is defined by Metal. It remains constant for the duration of a kernel’s execution, across dispatches of a given kernel with the same launch parameters, and from one threadgroup to another within the dispatch.

The number of threads in a SIMD group is returned by the [`threadExecutionWidth`](mtlcomputepipelinestate/threadexecutionwidth.md) of your compute pipeline state object. Attribute qualifiers allow you to access a SIMD group’s scalar index within a threadgroup, and a thread’s scalar index within a SIMD group:

Although threadgroups can be multidimensional, SIMD groups are 1D. Therefore, a thread’s position within a SIMD group is a scalar value for all threadgroup shapes. The SIMD group size remains constant and is unaffected by the threadgroup size.

For example, using the same 16 x 16 grid shown in [`Figure 2`](compute_passes/creating_threads_and_threadgroups#2929009.md), with a thread execution width of 16, a single 8 x 4 threadgroup consists of 2 SIMD groups. Because a SIMD group contains 16 threads, each SIMD group constitutes 2 rows in the threadgroup:

![A threadgroup composed of 2 SIMD groups.](https://docs-assets.developer.apple.com/published/85c2ac05dedad457f78499527ecec88a/media-2928945%402x.png)

The thread shown in red in [`Figure 5`](compute_passes/creating_threads_and_threadgroups#2929426.md) has a `[[simdgroup_index_in_threadgroup]]` value of 1 and a `[[thread_index_in_simdgroup]]` value of 1:

![The position of a single thread in a SIMD group.](https://docs-assets.developer.apple.com/published/604a6149e5d08c9ce8c3f7146c7e7e44/media-2929426%402x.png)

## See Also

- [Calculating threadgroup and grid sizes](calculating-threadgroup-and-grid-sizes.md)
  Calculate the optimum sizes for threadgroups and grids when dispatching compute-processing workloads.
- [protocol MTL4ComputeCommandEncoder](mtl4computecommandencoder.md)
  Encodes computation dispatches, resource copying commands, and acceleration structure building commands for a single pass into a command buffer.
- [protocol MTLComputeCommandEncoder](mtlcomputecommandencoder.md)
  Encodes computation dispatch commands for a single compute pass into a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/creating-threads-and-threadgroups)*