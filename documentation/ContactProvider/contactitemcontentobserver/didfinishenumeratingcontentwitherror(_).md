# didFinishEnumeratingContentWithError(_:)

**Framework**: ContactProvider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Finishes the content enumeration with an error, indicating failure, to the observer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func didFinishEnumeratingContentWithError(_: any Error)
```

## Discussion

Use [`ContactProviderError.pageExpired`](../contactprovidererror/pageexpired.md) to restart the content enumeration.

## See Also

### Ending enumeration
- [func didFinishEnumeratingContent(upTo: Data)](./didfinishenumeratingcontent%28upto%29.md)
  Finishes the content enumeration to the observer.
- [func didFinishEnumeratingPage(upTo: ContactItemPage)](./didfinishenumeratingpage%28upto%29.md)
  Marks a page of items as completed.
- [struct ContactItemPage](../contactitempage.md)
  A fixed offset into enumerating all contact items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemcontentobserver/didfinishenumeratingcontentwitherror(_:))*