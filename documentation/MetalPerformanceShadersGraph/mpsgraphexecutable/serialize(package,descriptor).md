# serialize(package:descriptor:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Serialize the MPSGraph executable at the provided url.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func serialize(package url: URL, descriptor: MPSGraphExecutableSerializationDescriptor?)
```

```objc
- (void) serializeToMPSGraphPackageAtURL:(NSURL *) url descriptor:(MPSGraphExecutableSerializationDescriptor *) descriptor;
```

## Parameters

- `url`: The URL where to serialize the MPSGraph executable.
- `descriptor`: The descriptor to be used to serialize the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutable/serialize(package:descriptor:))*