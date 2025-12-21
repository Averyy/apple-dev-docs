# canAddPasses()

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Returns a Boolean value that indicates whether the device supports adding passes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func canAddPasses() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the device supports adding passes; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [Wallet Developer Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/index.html#//apple_ref/doc/uid/TP40012195)
- [class func isPassLibraryAvailable() -> Bool](pkpasslibrary/ispasslibraryavailable.md)
  Returns a Boolean value that indicates whether the pass library is available.
- [class PKPassLibrary](pkpasslibrary.md)
  Provides an interface to the user’s library of passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/canaddpasses())*