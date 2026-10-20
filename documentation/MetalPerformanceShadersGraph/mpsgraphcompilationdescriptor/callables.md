# callables

**Framework**: Metal Performance Shaders Graph  
**Kind**: property  
**Role**: Instance Property

The dictionary used during runtime to lookup the [`MPSGraphExecutable`](../mpsgraphexecutable.md) which correspond to the `symbolName`.

**Availability**:
- iOS 17.1+
- iPadOS 17.1+
- Mac Catalyst 17.1+
- macOS 14.1+
- tvOS 17.1+
- visionOS 1.0+

## Declaration

```swift
var callables: [String : MPSGraphExecutable]? { get set }
```

```objc
@property (atomic, readwrite, nullable) MPSGraphCallableMap * callables;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphcompilationdescriptor/callables)*