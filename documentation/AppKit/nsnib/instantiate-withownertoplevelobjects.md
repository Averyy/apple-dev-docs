# instantiate(withOwner:topLevelObjects:)

**Framework**: AppKit  
**Kind**: method

Instantiates objects in the nib file with the specified owner.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func instantiate(withOwner owner: Any?, topLevelObjects: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the nib is instantiated; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Unlike legacy methods, the objects adhere to standard Cocoa memory management rules; it is necessary to keep a strong reference to the objects or the array to prevent the nib contents from being deallocated.

Outlets to top level objects should be strong references to demonstrate ownership and prevent deallocation.

## Parameters

- `owner`: The object to set as the Nib’s owner (File’s Owner).
- `topLevelObjects`: On return, an array containing the top-level objects of the nib.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsnib/instantiate(withowner:toplevelobjects:))*