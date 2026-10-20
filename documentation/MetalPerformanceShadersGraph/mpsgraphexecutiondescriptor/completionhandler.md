# completionHandler

**Framework**: Metal Performance Shaders Graph  
**Kind**: property  
**Role**: Instance Property

The handler that graph calls at the completion of the execution.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var completionHandler: MPSGraphCompletionHandler { get set }
```

```objc
@property (atomic, readwrite) MPSGraphCompletionHandler completionHandler;
```

#### Discussion

Default value is nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutiondescriptor/completionhandler)*