# invalidate()

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Cancels a currently-running enumeration, in respone to a call from the framework.

**Availability**:
- macOS 26.0+

## Declaration

```swift
func invalidate()
```

#### Discussion

The framework calls this method to cancel a search if the person using the device changes their query, making the results of the current search obsolete. The framework also calls this method when it’s finished using this enumerator object.

Implement this method by canceling any outstanding requests and cleaning up resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchenumerator/invalidate())*