# makeIntersectionFunction(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Synchronously creates an object representing a ray-tracing intersection function, using the specified descriptor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func makeIntersectionFunction(descriptor: MTLIntersectionFunctionDescriptor) throws -> any MTLFunction
```

```objc
- (id<MTLFunction>) newIntersectionFunctionWithDescriptor:(MTLIntersectionFunctionDescriptor *) descriptor error:(NSError **) error;
```

## See Also

### Creating intersection function instances
- [func makeIntersectionFunction(descriptor: MTLIntersectionFunctionDescriptor, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](./makeintersectionfunction%28descriptor,completionhandler%29.md)
  Asynchronously creates an object representing a ray-tracing intersection function, using the specified descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibrary/makeintersectionfunction(descriptor:))*