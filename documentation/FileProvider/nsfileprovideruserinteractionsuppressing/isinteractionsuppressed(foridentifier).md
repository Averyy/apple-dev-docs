# isInteractionSuppressed(forIdentifier:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the File Provider extension if the user suppressed the specified interaction.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func isInteractionSuppressed(forIdentifier suppressionIdentifier: String) -> Bool
```

```objc
- (BOOL) isInteractionSuppressedForIdentifier:(NSString *) suppressionIdentifier;
```

## Parameters

- `suppressionIdentifier`: A unique identifier for the user interaction.

## See Also

### Supressing Interactions
- [func setInteractionSuppressed(Bool, forIdentifier: String)](./setinteractionsuppressed%28_,foridentifier%29.md)
  Tells the File Provider extension that the user wants to suppress the user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideruserinteractionsuppressing/isinteractionsuppressed(foridentifier:))*