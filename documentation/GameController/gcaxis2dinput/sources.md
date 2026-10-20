# sources

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

One or more physical actions the user performs to manipulate the input.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.3+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var sources: Set<AnyHashable> { get }
```

```objc
@property (copy, readonly) NSSet<id<GCPhysicalInputSource>> * sources;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcaxis2dinput/sources)*