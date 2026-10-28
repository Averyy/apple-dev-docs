# writePlaceholder(at:withMetadata:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Type Method

Writes a document placeholder with the provided metadata.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 8.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`NSFileProviderManager`](../nsfileprovidermanager.md) class’s [`writePlaceholder(at:withMetadata:)`](../nsfileprovidermanager/writeplaceholder%28at,withmetadata%29.md) method instead.

## Declaration

```swift
class func writePlaceholder(at placeholderURL: URL, withMetadata metadata: [URLResourceKey : Any]) throws
```

```objc
+ (BOOL) writePlaceholderAtURL:(NSURL *) placeholderURL withMetadata:(NSDictionary<NSString *,id> *) metadata error:(NSError **) error;
```

## Discussion

Call this method whenever you need to create a placeholder for a document. The metadata that you provide depends largely on the needs of your document picker’s user interface; however, the common options include file size, filename, and thumbnails.

You must not override this method.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `placeholderURL`: The placeholder URL for the document. You can generate a placeholder URL from a document URL by calling [`placeholderURL(for:)`](./placeholderurl%28for%29.md).
- `metadata`: The metadata for this document.

## See Also

### Managing placeholders
- [class func placeholderURL(for: URL) -> URL](./placeholderurl%28for%29.md)
  Returns a placeholder URL for a given document URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/writeplaceholder(at:withmetadata:))*