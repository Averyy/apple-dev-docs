# saveAndReturnError()

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Saves all the changes made since the last save.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func saveAndReturnError() throws
```

```objc
- (BOOL) saveAndReturnError:(NSError **) error;
```

#### Discussion

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Saving and Detecting Changes
- [func hasUnsavedChanges() -> Bool](./hasunsavedchanges%28%29.md)
  Indicates whether an address book has changes that have not been saved to the Address Book database.
- [func save() -> Bool](./save%28%29.md)
  Saves all the changes made since the last save.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/saveandreturnerror())*