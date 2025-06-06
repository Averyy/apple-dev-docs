# controller

**Framework**: Game Controller  
**Kind**: property

The underlying controller object that you use to access input elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var controller: GCController? { get }
```

#### Discussion

Use this property to either get the element’s input values directly, or set handlers to get callbacks with the input values that changed. If you don’t connect the virtual controller to the device using `connect()`, this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller/controller)*