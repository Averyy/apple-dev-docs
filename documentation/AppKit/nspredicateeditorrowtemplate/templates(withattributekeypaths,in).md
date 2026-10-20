# templates(withAttributeKeyPaths:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns an array of predicate templates for the given attribute key paths for a given entity.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class func templates(withAttributeKeyPaths keyPaths: [String], in entityDescription: NSEntityDescription) -> [NSPredicateEditorRowTemplate]
```

```objc
+ (NSArray<NSPredicateEditorRowTemplate *> *) templatesWithAttributeKeyPaths:(NSArray<NSString *> *) keyPaths inEntityDescription:(NSEntityDescription *) entityDescription;
```

#### Return Value

An array of predicate templates for `keyPaths` originating at `entityDescription`.

#### Discussion

This method determines which key paths in the entity description can use the same views (that is, share the same attribute type). For each of these groups, it instantiates individual templates via [`init(leftExpressions:rightExpressions:modifier:operators:options:)`](./init%28leftexpressions,rightexpressions,modifier,operators,options%29.md).

## Parameters

- `keyPaths`: An array of attribute key paths originating at `entityDescription`. The key paths may cross relationships but must terminate in attributes.
- `entityDescription`: A Core Data entity description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/templates(withattributekeypaths:in:))*