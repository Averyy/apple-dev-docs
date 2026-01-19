---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/dataset.html
---

# Common operations

**

- [.rst](../_sources/python/dataset.rst)
- **

.pdf

**

# Common operations

 Table of contents 

## Contents

# Common operations

Both `Buffer` and `Stream` allow to apply transformations to
samples when they are accessed. These transformations share the same API which
is described below in terms of the `Buffer` class (but `Stream` is
identical). For the methods specific to `Buffer` or `Stream` see
the corresponding pages.

## General sample operations

| Buffer.batch(self, batch_size[, pad, dim]) | Creates batches frombatch_sizeconsecutive samples. |
| --- | --- |
| Buffer.filter_by_shape(self, key, dim[, ...]) | Filter samples based on the shape of the array. |
| Buffer.filter_key(self, key[, remove]) | Transform the samples to either only contain thiskeyor never contain thiskeybased on the value ofremove. |
| Buffer.key_transform(self, key, func[, ...]) | Apply the python functionfuncon the arrays in the selectedkey. |
| Buffer.sample_transform(self, func) | Apply the python functionfuncon whole samples. |
| Buffer.remove_value(self, key, size_key, ...) | Remove instances of a certain value from an array and shift the whole array to the left. |
| Buffer.rename_key(self, key, output_key) | Rename a sample key. |

## Image operations

| Buffer.image_center_crop(self, key, w, h[, ...]) | Center crop the image atkey. |
| --- | --- |
| Buffer.image_channel_reduction(self, key[, ...]) | Reduce an RGB image to gray-scale with various weights for red, green and blue. |
| Buffer.image_random_area_crop(self, key, ...) | Crop the image randomly such that the result is a portion of the original area and within the given aspect ratio range. |
| Buffer.image_random_crop(self, key, w, h[, ...]) | Extract a random crop of the requested size. |
| Buffer.image_random_h_flip(self, key, prob) | Horizontally flip the imageprobpercent of the time. |
| Buffer.image_resize(self, key, w, h[, ...]) | Resize the image to the requested size. |
| Buffer.image_resize_smallest_side(self, key, ...) | Resize the image such that its smallest side issize. |
| Buffer.image_rotate(self, key, angle[, ...]) | Rotate an image around its center point. |

## I/O operations

| Buffer.load_audio(self, key, prefix, info, ...) | Load an audio file. |
| --- | --- |
| Buffer.load_file(self, key[, prefix, output_key]) | Load the contents of a file. |
| Buffer.load_numpy(self, key[, prefix, ...]) | Load an array from a .npy file. |
| Buffer.load_image(self, key[, prefix, info, ...]) | Load an image file. |
| Buffer.load_video(self, key[, prefix, info, ...]) | Load a video file. |
| Buffer.read_from_tar(self, tarkey, ikey, ...) | Read data from tarfiles. |

## Padding operations

| Buffer.pad(self, key, dim, lpad, rpad, pad_value) | Pad the array atkey. |
| --- | --- |
| Buffer.pad_to_multiple(self, key, dim, ...) | Pad the end of an array such that its size is a multiple ofpad_multiple. |
| Buffer.pad_to_size(self, key, dim, size, ...) | Pad the end of an array such that its size issize. |

## Shape operations

| Buffer.shape(self, key, output_key[, dim]) | Extracts the shape of an array in the sample. |
| --- | --- |
| Buffer.shard(self, key, num_shards[, output_key]) | Split the first dimension innum_shards. |
| Buffer.squeeze(self, key[, dim, output_key]) | Squeeze singleton dimensions. |

## Tokenization

| Buffer.tokenize(self, key, trie, mode, ...) | Tokenize the contents of the array atkey. |
| --- | --- |

## Conditional operations

A common issue when writing pipelines is configuring them according to the
command line or configuration arguments. This usually results in code with a
lot of redirections that is hard to read and reason about what operations are
actually applied to the data.

For this reason all of the above methods have a conditional variant defined as
follows `*_if(cond: bool, *args, **kwargs)`. This allows writing pipelines
that read from top to bottom without having to resort to redirection statements
in python.

```
# Assuming we have a buffer with image files and labels in dset
dset = (
    dset
    .load_image("image_file", output_key="image")
    .image_random_crop_if(enable_random_crop, "image", 256, 256)
    .image_random_h_flip_if(flip_prob > 0, "image", flip_prob)
    .key_transform_if(brightness_range > 0, "image",
                      lambda x: ((1 + brightness_range * np.random.rand(x.shape[:2])[..., None]) * x).astype(x.dtype))
)
```

** Contents
