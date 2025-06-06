# SecPolicyGetTypeID()

**Framework**: Security  
**Kind**: func

Returns the unique identifier of the opaque type to which a policy object belongs.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecPolicyGetTypeID() -> CFTypeID
```

#### Return Value

A value that identifies the opaque type of a [`SecPolicy`](secpolicy.md) object.

#### Discussion

This function returns a value that uniquely identifies the opaque type of a [`SecPolicy`](secpolicy.md) object. You can compare this value to the [`CFTypeID`](https://developer.apple.com/documentation/CoreFoundation/CFTypeID) identifier obtained by calling the [`CFGetTypeID(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFGetTypeID(_:)) function on a specific object. These values might change from release to release or platform to platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpolicygettypeid())*