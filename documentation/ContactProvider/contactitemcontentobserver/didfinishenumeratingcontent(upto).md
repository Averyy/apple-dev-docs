# didFinishEnumeratingContent(upTo:)

**Framework**: ContactProvider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Finishes the content enumeration to the observer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func didFinishEnumeratingContent(upTo generationMarker: Data)
```

## Discussion

Call this when there are no more items to enumerate. Any future item enumerations after this are change enumerations. The first change enumeration begins from `generationMarker`, which syncs changes made after the content enumeration began. Calling this method saves the current page of items to the system Contacts database.

## Parameters

- `generationMarker`: A value specific to your data source identifying the database generation whose content has been enumerated.

## See Also

### Ending enumeration
- [func didFinishEnumeratingPage(upTo: ContactItemPage)](./didfinishenumeratingpage%28upto%29.md)
  Marks a page of items as completed.
- [struct ContactItemPage](../contactitempage.md)
  A fixed offset into enumerating all contact items.
- [func didFinishEnumeratingContentWithError(any Error)](./didfinishenumeratingcontentwitherror%28_%29.md)
  Finishes the content enumeration with an error, indicating failure, to the observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemcontentobserver/didfinishenumeratingcontent(upto:))*