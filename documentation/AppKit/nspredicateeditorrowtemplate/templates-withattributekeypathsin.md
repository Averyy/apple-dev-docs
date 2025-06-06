# templates(withAttributeKeyPaths:in:)

**Framework**: AppKit  
**Kind**: method

Returns an array of predicate templates for the given attribute key paths for a given entity.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class func templates(withAttributeKeyPaths keyPaths: [String], in entityDescription: NSEntityDescription) -> [NSPredicateEditorRowTemplate]
```

#### Return Value

An array of predicate templates for `keyPaths` originating at `entityDescription`.

#### Discussion

This method determines which key paths in the entity description can use the same views (that is, share the same attribute type). For each of these groups, it instantiates individual templates via [`init(leftExpressions:rightExpressions:modifier:operators:options:)`](nspredicateeditorrowtemplate/init(leftexpressions:rightexpressions:modifier:operators:options:).md).

## Parameters

- `keyPaths`: An array of attribute key paths originating at  . The key paths may cross relationships but must terminate in attributes.
- `entityDescription`: A Core Data entity description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/templates(withattributekeypaths:in:))*