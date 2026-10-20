# Coordinator

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

A type to coordinate with the WatchKit interface object.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
associatedtype Coordinator = Void
```

## See Also

### Providing a custom coordinator object
- [func makeCoordinator() -> Self.Coordinator](./makecoordinator%28%29.md)
  Creates the custom instance that you use to communicate changes from your interface object to other parts of your SwiftUI interface.
- [associatedtype WKInterfaceObjectType : WKInterfaceObject](./wkinterfaceobjecttype.md)
  The type of WatchKit interface object to be presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkinterfaceobjectrepresentable/coordinator)*