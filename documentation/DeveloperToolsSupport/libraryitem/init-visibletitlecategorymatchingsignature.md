# init(_:visible:title:category:matchingSignature:)

**Framework**: DeveloperToolsSupport  
**Kind**: init

Creates a new library item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init<SnippetExpressionType>(_ snippet: @autoclosure () -> SnippetExpressionType, visible: Bool = true, title: String? = nil, category: LibraryItem.Category = .other, matchingSignature: String? = nil)
```

## Parameters

- `snippet`: The expression to insert when the user picks the item   from the library, or inserts it via code completion.
- `visible`: A Boolean that specifies whether to make this item visible in the   library. You might choose to hide an item from the library if its only   purpose is to support code completion.
- `title`: A title for the item in the library.   If unspecified, Xcode generates a default title.
- `category`: A category for the item in the library.   If unspecified, Xcode assumes the default category of “Other”.
- `matchingSignature`: An overload for which the item presents its code   completion. You typically use this parameter when setting up an item as a   source of custom code completion. At the time of completion, the code   completion engine looks for an item matching the signature and   inserts its completion, if found.

## See Also

- [LibraryItem.Category](libraryitem/category.md)
  The kinds of library items that you can create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/libraryitem/init(_:visible:title:category:matchingsignature:))*