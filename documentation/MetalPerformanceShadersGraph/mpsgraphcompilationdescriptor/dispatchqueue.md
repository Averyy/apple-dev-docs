# dispatchQueue

**Framework**: Metal Performance Shaders Graph  
**Kind**: property  
**Role**: Instance Property

The dispatch queue used for the compilation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var dispatchQueue: dispatch_queue_t { get set }
```

```objc
@property (atomic, retain, readwrite) dispatch_queue_t dispatchQueue;
```

#### Discussion

Default value is nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphcompilationdescriptor/dispatchqueue)*