# instantiate(withOwner:topLevelObjects:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Instantiates objects in the nib file with the specified owner.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func instantiate(withOwner owner: Any?, topLevelObjects: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> Bool
```

```objc
- (BOOL) instantiateWithOwner:(id) owner topLevelObjects:(NSArray **) topLevelObjects;
```

## Return Value

[`true`](../../Swift/true.md) if the nib is instantiated; otherwise [`false`](../../Swift/false.md).

## Discussion

Unlike legacy methods, the objects adhere to standard Cocoa memory management rules; it is necessary to keep a strong reference to the objects or the array to prevent the nib contents from being deallocated.

Outlets to top level objects should be strong references to demonstrate ownership and prevent deallocation.

## Parameters

- `owner`: The object to set as the Nib’s owner (File’s Owner).
- `topLevelObjects`: On return, an array containing the top-level objects of the nib.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsnib/instantiate(withowner:toplevelobjects:))*