# output

**Framework**: Compute Graph  
**Kind**: namespace

A set of nodes for the output stage that adjust an element’s appearance without modifying its underlying state.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Topics

### Functions
- [void output::fadeInOut()](output/fadeinout.md)
  Applies a smooth fade-in and fade-out animation to the rendered output.
- [void output::growIn()](output/growin.md)
  Applies a smooth grow-in animation to the rendered output.
- [uint output::outputIndex()](output/outputindex.md)
  Returns the index of the current output element being processed.
- [float3 output::outputPosition()](output/outputposition.md)
  Returns the position of the rendered output.
- [void output::setColor(color)](output/setcolor.md)
  Sets the color of the rendered output.
- [void output::setOpacity(opacity)](output/setopacity.md)
  Sets the opacity of the rendered output.
- [void output::setOutputPosition(position)](output/setoutputposition.md)
  Sets the position of the rendered output.
- [void output::setScale(scale)](output/setscale.md)
  Sets the scale factor of the rendered output.
- [void output::setSize(size)](output/setsize.md)
  Sets the size of the rendered output.
- [void output::setUV2(value)](output/setuv2.md)
  Sets the second UV coordinate set for the rendered output mesh.
- [void output::setUV3(value)](output/setuv3.md)
  Sets the third UV coordinate set for the rendered output mesh.
- [void output::setUV4(value)](output/setuv4.md)
  Sets the fourth UV coordinate set for the rendered output mesh.
- [void output::setUV5(value)](output/setuv5.md)
  Sets the fifth UV coordinate set for the rendered output mesh.
- [void output::setUV6(value)](output/setuv6.md)
  Sets the sixth UV coordinate set for the rendered output mesh.
- [void output::setUV7(value)](output/setuv7.md)
  Sets the seventh UV coordinate set for the rendered output mesh.
- [void output::setUVTransform(uvOffset, uvScale)](output/setuvtransform.md)
  Sets the UV0 coordinate transformation for the rendered output.

## See Also

- [element](element.md)
  A set of nodes for reading and writing the current element within a particle simulation.
- [emitter](emitter.md)
  A set of nodes for the emission stage that control how often and how many elements a simulation spawns.
- [initialize](initialize.md)
  A set of nodes for the initialization stage that set an element’s starting state.
- [module](module.md)
  A set of nodes that mutate per-particle state, including position, velocity, color, size, and lifetime.
- [force](force.md)
  A set of nodes that apply physics forces to particles, including gravity, drag, noise, and twist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output)*