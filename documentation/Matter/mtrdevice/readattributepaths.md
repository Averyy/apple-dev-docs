# readAttributePaths(_:)

**Framework**: Matter  
**Kind**: method

Read the attributes identified by the provided attribute paths.  The paths can include wildcards.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
func readAttributePaths(_ attributePaths: [MTRAttributeRequestPath]) -> [[String : Any]]
```

#### Return Value

An array of response-value dictionaries as described in the documentation for MTRDeviceResponseHandler.  Each one will have an MTRAttributePathKey and an MTRDataKey.

#### Discussion

Paths that do not correspond to any existing attributes, or that the MTRDevice does not have attribute values for, will not be present in the return value from this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevice/readattributepaths(_:))*