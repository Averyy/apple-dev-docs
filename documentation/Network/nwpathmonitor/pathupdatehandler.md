# pathUpdateHandler

**Framework**: Network  
**Kind**: property

A handler that receives network path updates.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@preconcurrency
final var pathUpdateHandler: ((NWPath) -> Void)? { get set }
```

## See Also

- [var currentPath: NWPath](nwpathmonitor/currentpath.md)
  The currently available network path observed by the path monitor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwpathmonitor/pathupdatehandler)*