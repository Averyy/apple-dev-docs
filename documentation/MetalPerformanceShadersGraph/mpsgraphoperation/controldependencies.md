# controlDependencies

**Framework**: Metal Performance Shaders Graph  
**Kind**: property  
**Role**: Instance Property

The set of operations guaranteed to execute before this operation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var controlDependencies: [MPSGraphOperation] { get }
```

```objc
@property (nonatomic, readonly, nonnull) NSArray<MPSGraphOperation *> * controlDependencies;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphoperation/controldependencies)*