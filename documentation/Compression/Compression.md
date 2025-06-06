# Compression

**Framework**: Compression  
**Kind**: module

Leverage common compression algorithms for lossless data compression.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

#### Overview

The Compression framework enables your app to provide lossless compression when saving or sharing files and data. Compression is a process in which you compress (encode) and decompress (decode) data. For example, a text editor may save its files in a compressed format, and automatically decompress the saved file when the user opens it.

![A flow diagram that illustrates the compression and decompression process. The encoder compresses the original data into the encoded (compressed) data. The decoder decompresses the encoded data into the decompressed data.](https://docs-assets.developer.apple.com/published/b37d3585a0d73570be20ff8da0ec06f3/media-4311255%402x.png)

The framework offers two methods of compression:

-  uses a single-step method for compressing files, making it perfect for use with uncompressed files under 8 MB, or compressed files under 1 MB.
-  uses multiple steps for compressing files, making it ideal for compressing larger files or streamed data, such as an incoming audio signal or downloading files.

To use buffer compression, you compress or decompress the input data with one call to the corresponding function. To learn more about buffer compression, including a walk-through of the code used to encode and decode a string, see [`Compressing and decompressing data with buffer compression`](https://developer.apple.com/documentation/Accelerate/compressing-and-decompressing-data-with-buffer-compression).

To use stream compression, you call the compression or decompression function repeatedly to compress or decompress data from a source buffer to a destination buffer. Between calls, the compressor or decompressor moves processed data out of the source buffer and loads new data into the destination buffer. To learn more about stream compression, see the sample code project [`Compressing and decompressing files with stream compression`](https://developer.apple.com/documentation/Accelerate/compressing-and-decompressing-files-with-stream-compression).

## Topics

### Objects that simplify multiple-step compression
- [Compressing and decompressing data with input and output filters](../Accelerate/compressing-and-decompressing-data-with-input-and-output-filters.md)
  Compress and decompress streamed or from-memory data, using input and output filters.
- [Compressing and decompressing files with stream compression](../Accelerate/compressing-and-decompressing-files-with-stream-compression.md)
  Perform compression for all files and decompression for files with supported extension types.
- [class InputFilter](inputfilter.md)
  An encoder-decoder that reads input data from a stream.
- [class OutputFilter](outputfilter.md)
  An encoder-decoder that writes output data to a stream.
- [enum Algorithm](algorithm.md)
  Algorithms used for compression or decompression.
- [enum FilterError](filtererror.md)
  Errors that occur during compression.
- [enum FilterOperation](filteroperation.md)
  Operations that define whether input and output filters compress or decompress data.
### Multiple-step compression
- [struct compression_stream](compression_stream.md)
  A structure representing a compression stream.
- [func compression_stream_init(UnsafeMutablePointer<compression_stream>, compression_stream_operation, compression_algorithm) -> compression_status](compression_stream_init(_:_:_:).md)
  Initializes a compression stream for either compression or decompression.
- [func compression_stream_process(UnsafeMutablePointer<compression_stream>, Int32) -> compression_status](compression_stream_process(_:_:).md)
  Performs compression or decompression using an initialized compression stream structure.
- [func compression_stream_destroy(UnsafeMutablePointer<compression_stream>) -> compression_status](compression_stream_destroy(_:).md)
  Frees any memory allocated by stream initialization function.
- [struct compression_status](compression_status.md)
  A set of values used to represent the status of stream compression.
- [struct compression_stream_flags](compression_stream_flags.md)
  A set of values used to represent stream compression flags.
- [struct compression_stream_operation](compression_stream_operation.md)
  A set of values used to represent a stream compression operation.
- [struct compression_algorithm](compression_algorithm.md)
  A structure for values that represent compression algorithms.
### Single-step compression
- [Compressing and decompressing data with buffer compression](../Accelerate/compressing-and-decompressing-data-with-buffer-compression.md)
  Compress a string, write it to the file system, and decompress the same file using buffer compression.
- [func compression_encode_scratch_buffer_size(compression_algorithm) -> Int](compression_encode_scratch_buffer_size(_:).md)
  Returns the required compression scratch buffer size for the selected algorithm.
- [func compression_encode_buffer(UnsafeMutablePointer<UInt8>, Int, UnsafePointer<UInt8>, Int, UnsafeMutableRawPointer?, compression_algorithm) -> Int](compression_encode_buffer(_:_:_:_:_:_:).md)
  Compresses the contents of a source buffer into a destination buffer.
- [func compression_decode_scratch_buffer_size(compression_algorithm) -> Int](compression_decode_scratch_buffer_size(_:).md)
  Returns the required decompression scratch buffer size for the selected algorithm.
- [func compression_decode_buffer(UnsafeMutablePointer<UInt8>, Int, UnsafePointer<UInt8>, Int, UnsafeMutableRawPointer?, compression_algorithm) -> Int](compression_decode_buffer(_:_:_:_:_:_:).md)
  Decompresses the contents of a source buffer into a destination buffer.
- [struct compression_algorithm](compression_algorithm.md)
  A structure for values that represent compression algorithms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Compression)*