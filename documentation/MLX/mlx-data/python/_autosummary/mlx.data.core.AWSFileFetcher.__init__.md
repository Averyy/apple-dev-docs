---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.core.AWSFileFetcher.__init__.html
---

# mlx.data.core.AWSFileFetcher.__init__

**

- [.rst](../../_sources/python/_autosummary/mlx.data.core.AWSFileFetcher.__init__.rst)
- **

.pdf

**

# mlx.data.core.AWSFileFetcher.__init__

 Table of contents 

## Contents

# mlx.data.core.AWSFileFetcher.__init__

**AWSFileFetcher.__init__(*self: mlx.data._c.core.AWSFileFetcher*, *bucket: str*, *endpoint: str = ''*, *region: str = ''*, *prefix: os.PathLike = ''*, *local_prefix: os.PathLike = ''*, *ca_bundle: str = ''*, *virtual_host: bool = False*, *verify_ssl: bool = True*, *connect_timeout_ms: int = 1000*, *num_retry_max: int = 10*, *num_connection_max: int = 25*, *buffer_size: int = 104857600*, *num_threads: int = 4*, *num_prefetch_max: int = 1*, *num_prefetch_threads: int = 1*, *num_kept_files: int = 0*, *access_key_id: str = ''*, *secret_access_key: str = ''*, *session_token: str = ''*, *expiration: str = ''*, *verbose: bool = False*) → [None](https://docs.python.org/3/library/constants.html#None)**
: Make an AWSFileFetcher to fetch files from S3.

Parameters:

**bucket** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The S3 bucket to use.
**endpoint** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The endpoint to use.
**region** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The region to use.
**prefix** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The remote prefix to use for all files requested. (default: ‘’)
**local_prefix** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The local cache directory to save the downloaded files in. (default: ‘’)
**ca_bundle** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The path to a certificate authority file for
establishing SSL/TLS connections. The environment variable
AWS_CA_BUNDLE can also be used instead. (default: ‘’)
**virtual_host** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Whether to use virtual hosted style urls (ie
the bucket in the domain part of the url). (default: false)
**verify_ssl** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Whether we should verify SSL certificates. (default: true)
**connect_timeout_ms** ([int](https://docs.python.org/3/library/functions.html#int)) – Assume it is a timeout after that many
milliseconds. (default: 1000)
**num_retry_max** ([int](https://docs.python.org/3/library/functions.html#int)) – How many times should we attempt to fetch a
file before deciding that we failed. The retry strategy is
exponential backoff. (default: 10)
**num_connection_max** ([int](https://docs.python.org/3/library/functions.html#int)) – Specifies the maximum number of HTTP
connections to the server. (default: 25)
**buffer_size** ([int](https://docs.python.org/3/library/functions.html#int)) – Fetch the files in parts of that size. (default: 100MB)
**num_threads** ([int](https://docs.python.org/3/library/functions.html#int)) – How many parts to fetch in parallel for each file. (default: 4)
**num_prefetch_max** ([int](https://docs.python.org/3/library/functions.html#int)) – How many files to prefetch from the prefetch list. (default: 1)
**num_prefetch_threads** ([int](https://docs.python.org/3/library/functions.html#int)) – How many files to prefetch in parallel from the prefetch list. (default: 1)
**num_kept_files** ([int](https://docs.python.org/3/library/functions.html#int)) – How many files to keep in the local cache.
If 0 we keep everything however if the files are larger than our
local disk this should be set to a positive number. (default: 0)
**access_key_id** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – Set the AWS access key id to authenticate to
the remote service. (default: ‘’)
**secret_access_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – Set the AWS secret access key id to
authenticate to the remote service. (default: ‘’)
**session_token** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – Set the AWS session token to authenticate to
the remote service. (default: ‘’)
**expiration** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – A date string defining the expiration of the
authentication credentials (default: ‘’)
**verbose** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Defines whether the file fetcher should write
information messages to the standard output. (default: false)

** Contents
