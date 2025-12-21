# SecTrustCopyProperties(_:)

**Framework**: Security  
**Kind**: func

Returns an array containing the properties of a trust object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func SecTrustCopyProperties(_ trust: SecTrust) -> CFArray?
```

#### Return Value

An array, or `NULL` if the trust object has not yet been evaluated. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to free this array’s memory when you are done with it.

#### Discussion

The result is an ordered array of dictionaries, one per certificate in the chain, beginning with the leaf node at index zero (`0`) and continuing up to the anchor (or the last certificate in the chain if no anchor was found).

The property dictionary at index zero may also include general information about the entire chain’s validity in the context of this trust evaluation. See [`Certificate Property Type Values`](certificate-property-type-values.md) for a list of currently defined keys.

## Parameters

- `trust`: The trust object from which properties should be copied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustcopyproperties(_:))*