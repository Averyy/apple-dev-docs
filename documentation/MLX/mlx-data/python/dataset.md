---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/dataset.html
---

# Common operations

Both `Buffer` and `Stream` allow to apply transformations to
samples when they are accessed. These transformations share the same API which
is described below in terms of the `Buffer` class (but `Stream` is
identical). For the methods specific to `Buffer` or `Stream` see
the corresponding pages.

## General sample operations

| [Buffer.batch](_autosummary/mlx.data.Buffer.batch.md#mlx.data.Buffer.batch)(self, batch_size[, pad, dim]) | Creates batches from `batch_size` consecutive samples. |
| --- | --- |
| [Buffer.filter_by_shape](_autosummary/mlx.data.Buffer.filter_by_shape.md#mlx.data.Buffer.filter_by_shape)(self, key, dim[, ...]) | Filter samples based on the shape of the array. |
| [Buffer.filter_key](_autosummary/mlx.data.Buffer.filter_key.md#mlx.data.Buffer.filter_key)(self, key[, remove]) | Transform the samples to either only contain this `key` or never contain this `key` based on the value of `remove`. |
| [Buffer.key_transform](_autosummary/mlx.data.Buffer.key_transform.md#mlx.data.Buffer.key_transform)(self, key, func[, ...]) | Apply the python function `func` on the arrays in the selected `key`. |
| [Buffer.sample_transform](_autosummary/mlx.data.Buffer.sample_transform.md#mlx.data.Buffer.sample_transform)(self, func) | Apply the python function `func` on whole samples. |
| [Buffer.remove_value](_autosummary/mlx.data.Buffer.remove_value.md#mlx.data.Buffer.remove_value)(self, key, size_key, ...) | Remove instances of a certain value from an array and shift the whole array to the left. |
| [Buffer.rename_key](_autosummary/mlx.data.Buffer.rename_key.md#mlx.data.Buffer.rename_key)(self, key, output_key) | Rename a sample key. |

## Image operations

| [Buffer.image_center_crop](_autosummary/mlx.data.Buffer.image_center_crop.md#mlx.data.Buffer.image_center_crop)(self, key, w, h[, ...]) | Center crop the image at `key`. |
| --- | --- |
| [Buffer.image_channel_reduction](_autosummary/mlx.data.Buffer.image_channel_reduction.md#mlx.data.Buffer.image_channel_reduction)(self, key[, ...]) | Reduce an RGB image to gray-scale with various weights for red, green and blue. |
| [Buffer.image_random_area_crop](_autosummary/mlx.data.Buffer.image_random_area_crop.md#mlx.data.Buffer.image_random_area_crop)(self, key, ...) | Crop the image randomly such that the result is a portion of the original area and within the given aspect ratio range. |
| [Buffer.image_random_crop](_autosummary/mlx.data.Buffer.image_random_crop.md#mlx.data.Buffer.image_random_crop)(self, key, w, h[, ...]) | Extract a random crop of the requested size. |
| [Buffer.image_random_h_flip](_autosummary/mlx.data.Buffer.image_random_h_flip.md#mlx.data.Buffer.image_random_h_flip)(self, key, prob) | Horizontally flip the image `prob` percent of the time. |
| [Buffer.image_resize](_autosummary/mlx.data.Buffer.image_resize.md#mlx.data.Buffer.image_resize)(self, key, w, h[, ...]) | Resize the image to the requested size. |
| [Buffer.image_resize_smallest_side](_autosummary/mlx.data.Buffer.image_resize_smallest_side.md#mlx.data.Buffer.image_resize_smallest_side)(self, key, ...) | Resize the image such that its smallest side is `size`. |
| [Buffer.image_rotate](_autosummary/mlx.data.Buffer.image_rotate.md#mlx.data.Buffer.image_rotate)(self, key, angle[, ...]) | Rotate an image around its center point. |

## I/O operations

| [Buffer.load_audio](_autosummary/mlx.data.Buffer.load_audio.md#mlx.data.Buffer.load_audio)(self, key, prefix, info, ...) | Load an audio file. |
| --- | --- |
| [Buffer.load_file](_autosummary/mlx.data.Buffer.load_file.md#mlx.data.Buffer.load_file)(self, key[, prefix, output_key]) | Load the contents of a file. |
| [Buffer.load_numpy](_autosummary/mlx.data.Buffer.load_numpy.md#mlx.data.Buffer.load_numpy)(self, key[, prefix, ...]) | Load an array from a .npy file. |
| [Buffer.load_image](_autosummary/mlx.data.Buffer.load_image.md#mlx.data.Buffer.load_image)(self, key[, prefix, info, ...]) | Load an image file. |
| [Buffer.load_video](_autosummary/mlx.data.Buffer.load_video.md#mlx.data.Buffer.load_video)(self, key[, prefix, info, ...]) | Load a video file. |
| [Buffer.read_from_tar](_autosummary/mlx.data.Buffer.read_from_tar.md#mlx.data.Buffer.read_from_tar)(self, tarkey, ikey, ...) | Read data from tarfiles. |

## Padding operations

| [Buffer.pad](_autosummary/mlx.data.Buffer.pad.md#mlx.data.Buffer.pad)(self, key, dim, lpad, rpad, pad_value) | Pad the array at `key`. |
| --- | --- |
| [Buffer.pad_to_multiple](_autosummary/mlx.data.Buffer.pad_to_multiple.md#mlx.data.Buffer.pad_to_multiple)(self, key, dim, ...) | Pad the end of an array such that its size is a multiple of `pad_multiple`. |
| [Buffer.pad_to_size](_autosummary/mlx.data.Buffer.pad_to_size.md#mlx.data.Buffer.pad_to_size)(self, key, dim, size, ...) | Pad the end of an array such that its size is `size`. |

## Shape operations

| [Buffer.shape](_autosummary/mlx.data.Buffer.shape.md#mlx.data.Buffer.shape)(self, key, output_key[, dim]) | Extracts the shape of an array in the sample. |
| --- | --- |
| [Buffer.shard](_autosummary/mlx.data.Buffer.shard.md#mlx.data.Buffer.shard)(self, key, num_shards[, output_key]) | Split the first dimension in `num_shards`. |
| [Buffer.squeeze](_autosummary/mlx.data.Buffer.squeeze.md#mlx.data.Buffer.squeeze)(self, key[, dim, output_key]) | Squeeze singleton dimensions. |

## Tokenization

| [Buffer.tokenize](_autosummary/mlx.data.Buffer.tokenize.md#mlx.data.Buffer.tokenize)(self, key, trie, mode, ...) | Tokenize the contents of the array at `key`. |
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
