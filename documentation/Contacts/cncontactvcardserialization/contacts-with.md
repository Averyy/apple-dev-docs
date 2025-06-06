# contacts(with:)

**Framework**: Contacts  
**Kind**: method

Returns the contacts from the vCard data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func contacts(with data: Data) throws -> [CNContact]
```

#### Return Value

An array of contacts.

#### Discussion

> **Note**: In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and [`About Imported Cocoa Error Parameters`](https://developer.apple.com/documentation/Swift/about-imported-cocoa-error-parameters).

## Parameters

- `data`: The vCard data representing one or more contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactvcardserialization/contacts(with:))*