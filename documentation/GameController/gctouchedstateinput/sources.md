# sources

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

One or more physical actions the user performs to manipulate the input.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var sources: Set<AnyHashable> { get }
```

```objc
@property (copy, readonly) NSSet<id<GCPhysicalInputSource>> * sources;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gctouchedstateinput/sources)*