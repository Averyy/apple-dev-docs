# externalObjects

**Framework**: UIKit  
**Kind**: property

The replacements for any proxy objects in the nib file.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
static let externalObjects: UINib.OptionsKey
```

#### Discussion

The value for this key is an [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) object. The keys of the dictionary are the names of any proxy objects in the nib file, and the value for each key is the actual object to use in place of the proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinib/optionskey/externalobjects)*