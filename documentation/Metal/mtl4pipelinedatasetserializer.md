# MTL4PipelineDataSetSerializer

**Framework**: Metal  
**Kind**: protocol

A fast-addition container for collecting data during pipeline state creation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol MTL4PipelineDataSetSerializer : NSObjectProtocol
```

## Mentions

- [Using the Metal 4 compilation API](using-the-metal-4-compilation-api.md)

#### Overview

Pipeline data serializer instances allow you to create binary archives and serialize pipeline scripts to use with the offline Metal binary generator (`metal-tt`) doc:compiling-binary-archives-from-a-custom-configuration-script.md.

You capture and retain all relevant data for all pipelines a compiler instance creates by providing an instance of this object to its [`MTL4CompilerDescriptor`](mtl4compilerdescriptor.md).

After capturing data, you can serialize it to a binary archive to persist its contents offline by calling [`serializeAsArchiveAndFlush(url:)`](mtl4pipelinedatasetserializer/serializeasarchiveandflush(url:).md). You can also serialize a pipeline script suitable for the offline binary generator (`metal-tt`) by calling [`serializeAsPipelinesScript()`](mtl4pipelinedatasetserializer/serializeaspipelinesscript().md)

> **Note**: The objects [`MTL4PipelineDataSetSerializer`](mtl4pipelinedatasetserializer.md) contains are opaque and can’t accelerate compilation for compilers they are not attached to. Additionally, your program can’t read data out of data set serializer instances.

## Topics

### Instance Methods
- [func serializeAsArchiveAndFlush(url: URL) throws](mtl4pipelinedatasetserializer/serializeasarchiveandflush(url:).md)
  Serializes a pipeline data set to an archive.
- [func serializeAsPipelinesScript() throws -> Data](mtl4pipelinedatasetserializer/serializeaspipelinesscript.md)
  Serializes a serializer data set to a pipeline script as raw data.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct MTL4PipelineDataSetSerializerConfiguration](mtl4pipelinedatasetserializerconfiguration.md)
  Configuration options for pipeline dataset serializer objects.
- [class MTL4PipelineDataSetSerializerDescriptor](mtl4pipelinedatasetserializerdescriptor.md)
  Groups together properties to create a pipeline data set serializer.
- [class MTL4PipelineDescriptor](mtl4pipelinedescriptor.md)
  Base type for descriptors you use for building pipeline state objects.
- [class MTL4PipelineOptions](mtl4pipelineoptions.md)
  Provides options controlling how to compile a pipeline state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4pipelinedatasetserializer)*