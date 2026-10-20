# dismantleWKInterfaceObject(_:coordinator:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method  
**Required**: Yes

Cleans up the presented WatchKit interface object (and its coordinator) in anticipation of their removal.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency static func dismantleWKInterfaceObject(_ wkInterfaceObject: Self.WKInterfaceObjectType, coordinator: Self.Coordinator)
```

#### Discussion

Use this method to perform additional clean-up work related to your custom interface object. For example, you might use this method to remove observers or update other parts of your SwiftUI interface.

## Parameters

- `wkInterfaceObject`: Your custom interface object.
- `coordinator`: The custom coordinator instance you use to communicate changes back to SwiftUI. If you do not use a custom coordinator, the system provides a default instance.

## Default Implementations

### WKInterfaceObjectRepresentable Implementations
- [static func dismantleWKInterfaceObject(Self.WKInterfaceObjectType, coordinator: Self.Coordinator)](./dismantlewkinterfaceobject%28_,coordinator%29-qd0y.md)
  Cleans up the presented interface object (and coordinator) in anticipation of their removal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkinterfaceobjectrepresentable/dismantlewkinterfaceobject(_:coordinator:))*