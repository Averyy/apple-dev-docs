---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/miscellaneous.html
---

# Miscellaneous

## FileFetcher

Several functions in MLX data can make use of a `FileFetcher` object to
fetch files from a remote location. See the [installation instructions](../install.md#install) to build MLX data with AWS support which adds the
`core.AWSFileFetcher` described below.

| [core.AWSFileFetcher.__init__](_autosummary/mlx.data.core.AWSFileFetcher.__init__.md#mlx.data.core.AWSFileFetcher.__init__)(self, bucket[, ...]) | Make an AWSFileFetcher to fetch files from S3. |
| --- | --- |
| [core.AWSFileFetcher.fetch](_autosummary/mlx.data.core.AWSFileFetcher.fetch.md#mlx.data.core.AWSFileFetcher.fetch)(self, filename) | Ensures the filename is in the local cache. |
| [core.AWSFileFetcher.prefetch](_autosummary/mlx.data.core.AWSFileFetcher.prefetch.md#mlx.data.core.AWSFileFetcher.prefetch)(self, filenames) | Start prefetching these files. |

A `FileFetcher` can also be used standalone in your scripts to
efficiently fetch remote content in background threads.

```
from pathlib import Path
from mlx.data.core import AWSFileFetcher

LOCAL_CACHE = Path("/path/to/local/cache")

ff = AWSFileFetcher(
    "my-cool-bucket",
    endpoint="https://my.endpoint.com/"
    local_prefix=LOCAL_CACHE,
    num_kept_files=100,
)

# When fetch returns my/remote/path/foo.npy will be in LOCAL_CACHE
ff.fetch("my/remote/path/foo.npy")
assert (LOCAL_CACHE / "my/remote/path/foo.npy").is_file()

# We can prefetch in the background
ff.prefetch(["foo_1.npy", "foo_2.npy"])
ff.fetch("foo_1.npy")
# process foo_1 while foo_2 downloads in the background
```
