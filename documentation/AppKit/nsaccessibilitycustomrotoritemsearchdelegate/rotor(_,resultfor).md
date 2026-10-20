# rotor(_:resultFor:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Performs a search with the specified search parameters and returns the item result.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func rotor(_ rotor: NSAccessibilityCustomRotor, resultFor searchParameters: NSAccessibilityCustomRotor.SearchParameters) -> NSAccessibilityCustomRotor.ItemResult?
```

```objc
- (NSAccessibilityCustomRotorItemResult *) rotor:(NSAccessibilityCustomRotor *) rotor resultForSearchParameters:(NSAccessibilityCustomRotorSearchParameters *) searchParameters;
```

## See Also

### Finding the Next Item
- [NSAccessibilityCustomRotor.SearchParameters](../nsaccessibilitycustomrotor/searchparameters.md)
  Search parameters for a custom rotor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotoritemsearchdelegate/rotor(_:resultfor:))*