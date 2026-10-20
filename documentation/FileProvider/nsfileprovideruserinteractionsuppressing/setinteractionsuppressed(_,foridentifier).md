# setInteractionSuppressed(_:forIdentifier:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the File Provider extension that the user wants to suppress the user interaction.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func setInteractionSuppressed(_ suppression: Bool, forIdentifier suppressionIdentifier: String)
```

```objc
- (void) setInteractionSuppressed:(BOOL) suppression forIdentifier:(NSString *) suppressionIdentifier;
```

## Parameters

- `suppression`: A Boolean value that indicates whether the user wants to suppress the specified user interaction.
- `suppressionIdentifier`: A unique identifier for the user interaction.

## See Also

### Supressing Interactions
- [func isInteractionSuppressed(forIdentifier: String) -> Bool](./isinteractionsuppressed%28foridentifier%29.md)
  Asks the File Provider extension if the user suppressed the specified interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideruserinteractionsuppressing/setinteractionsuppressed(_:foridentifier:))*