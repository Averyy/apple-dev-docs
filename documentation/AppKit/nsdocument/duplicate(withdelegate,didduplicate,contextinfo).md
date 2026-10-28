# duplicate(withDelegate:didDuplicate:contextInfo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a new document whose contents are the same as the current document.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func duplicate(withDelegate delegate: Any?, didDuplicate didDuplicateSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

```objc
- (void) duplicateDocumentWithDelegate:(id) delegate didDuplicateSelector:(SEL) didDuplicateSelector contextInfo:(void *) contextInfo;
```

## Discussion

The new document that is created doesn’t yet have a value to return from [`fileURL`](./fileurl.md). When duplicating is completed, regardless of success or failure, or whether the operation is rejected by the user, this method sends the message indicated by `didDuplicateSelector` to the delegate, with `contextInfo` as the last argument. The method selected by `didDuplicateSelector` must have the same signature as:

```objc
- (void)document:(NSDocument *)document didDuplicate:(BOOL)didDuplicate contextInfo:(void *)contextInfo;
```

The default implementation of this method first makes sure that any editor registered using the Cocoa Bindings `NSEditorRegistration` informal protocol has committed its changes, then checks to see if there are recent changes that might have been inadvertent and, if so, presents a panel giving the user the choice of canceling, duplicating, or duplicating then discarding recent changes. Unless the user cancels duplicating, or if no panel was presented, it then invokes [`duplicate()`](./duplicate%28%29.md). If the user chose duplicating and discarding, it also discards recent changes after duplicating.

## Parameters

- `delegate`: The delegate to which the selector message is sent.
- `didDuplicateSelector`: The selector of the message sent to the delegate.
- `contextInfo`: Object passed with the callback to provide any additional context information.

## See Also

### Duplicating the Document
- [func duplicate() throws -> NSDocument](./duplicate%28%29.md)
  Creates a new document whose contents are the same as the receiver and returns an error object if unsuccessful.
- [func duplicate(Any?)](./duplicate%28_%29.md)
  Creates a copy of the receiving document in response to the user choosing Duplicate from the File menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/duplicate(withdelegate:didduplicate:contextinfo:))*