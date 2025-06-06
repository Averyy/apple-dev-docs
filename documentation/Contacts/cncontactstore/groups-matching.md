# groups(matching:)

**Framework**: Contacts  
**Kind**: method

Fetches all groups matching the specified predicate.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func groups(matching predicate: NSPredicate?) throws -> [CNGroup]
```

#### Return Value

An array of [`CNGroup`](cngroup.md) objects that match the predicate.

#### Discussion

This method returns an empty array when no matching groups are found. If an error occurs, this method returns `nil`. You should use only the predicates defined in [`CNGroup`](cngroup.md) class predicates. Compound predicates are not supported. Contacts may be members of one or more groups, depending upon the account they come from.

> **Note**: In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and [`About Imported Cocoa Error Parameters`](https://developer.apple.com/documentation/Swift/about-imported-cocoa-error-parameters).

In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and [`About Imported Cocoa Error Parameters`](https://developer.apple.com/documentation/Swift/about-imported-cocoa-error-parameters).

## Parameters

- `predicate`: The predicate to use to fetch the matching groups. Set predicate to   to match all groups.

## See Also

- [func defaultContainerIdentifier() -> String](cncontactstore/defaultcontaineridentifier.md)
  Returns the identifier of the default container.
- [func containers(matching: NSPredicate?) throws -> [CNContainer]](cncontactstore/containers(matching:).md)
  Fetches all containers matching the specified predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactstore/groups(matching:))*