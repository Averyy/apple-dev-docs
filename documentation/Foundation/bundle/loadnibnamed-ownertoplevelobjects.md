# loadNibNamed(_:owner:topLevelObjects:)

**Framework**: Foundation  
**Kind**: method

Loads a nib from the bundle with the specified file name and owner.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func loadNibNamed(_ nibName: NSNib.Name, owner: Any?, topLevelObjects: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the nib file was loaded successfully; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Unlike legacy methods, the objects adhere to the standard cocoa memory management rules; it is necessary to keep a strong reference to them by using IBOutlets or holding a reference to the array to prevent the nib contents from being deallocated.

Outlets to top-level objects should be strong references to demonstrate ownership and prevent deallocation.

For more information on Nibs, see [`NSNib`](https://developer.apple.com/documentation/AppKit/NSNib).

## Parameters

- `nibName`: The name of the nib.
- `owner`: The object that will be the nib’s owner.
- `topLevelObjects`: This by-reference parameter is populated with the top level objects of the nib.

## See Also

- [func loadNibNamed(String, owner: Any?, options: [UINib.OptionsKey : Any]?) -> [Any]?](bundle/loadnibnamed(_:owner:options:).md)
  Unarchives the contents of a nib file located in the receiver’s bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/loadnibnamed(_:owner:toplevelobjects:))*