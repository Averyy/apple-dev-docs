# addItem(with:title:previewText:)

**Framework**: Safari Services  
**Kind**: method

Adds an item to the Reading List.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func addItem(with URL: URL, title: String?, previewText: String?) throws
```

#### Discussion

Call this method when the user chooses to add to the Reading List.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `URL`: The URL of the item.
- `title`: The title of the item, or  .
- `previewText`: A string shown as detail text for the item, or  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/ssreadinglist/additem(with:title:previewtext:))*