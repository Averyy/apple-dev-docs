# representedObject

**Framework**: AppKit  
**Kind**: property

The object whose value is presented in the receiver’s primary view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var representedObject: Any? { get set }
```

#### Discussion

This property  the object you provide to it; it does not  it. In another words, a view controller has a  relationship with its represented object and does not own it as an attribute.

The [`representedObject`](nsviewcontroller/representedobject.md) property is key-value coding and key-value observing compliant. When you use the represented object as the file’s owner of a nib file, you can bind controls to the file’s owner using key paths that start with the string `representedObject`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/representedobject)*