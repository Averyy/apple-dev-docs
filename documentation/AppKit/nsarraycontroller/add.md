# add(_:)

**Framework**: AppKit  
**Kind**: method

Creates and adds a new object to the receiver’s content and arranged objects.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
func add(_ sender: Any?)
```

#### Discussion

Beginning with OS X v10.4 the result of this method is deferred until the next iteration of the runloop so that the error presentation mechanism can provide feedback as a sheet.

## Parameters

- `sender`: Typically the object that invoked this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/add(_:))*