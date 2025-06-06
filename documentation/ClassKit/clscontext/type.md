# type

**Framework**: ClassKit  
**Kind**: property

The kind of content a context represents.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var type: CLSContextType { get }
```

#### Discussion

The context type helps teachers to understand what kind of assignable content you offer. The type doesn’t affect the behavior of the context, but it does appear to teachers as they browse your app’s content. This helps teachers better understand your content and how they might use it as part of their own lesson plans.

Use one of the values from [`CLSContextType`](clscontexttype.md). If you can’t find an exact match for your particular content, you might be able to find a similar one. For example, for an app that allows students to read plays, you might use [`CLSContextType.book`](clscontexttype/book.md), [`CLSContextType.chapter`](clscontexttype/chapter.md), and [`CLSContextType.section`](clscontexttype/section.md) as the types for the play, its acts, and their scenes, respectively.

Alternatively, you can use the [`CLSContextType.custom`](clscontexttype/custom.md) type, and provide a name for the type using the [`customTypeName`](clscontext/customtypename.md) property. The system presents this name to the user directly, so you should provide a localized value. If you choose the custom type but don’t provide a name, the system uses a localized default, like “Custom”. If you choose a type besides the custom type, the system ignores the custom type name.

## See Also

- [func setType(CLSContextType)](clscontext/settype(_:).md)
  Updates the kind of content that a context represents.
- [enum CLSContextType](clscontexttype.md)
  The kinds of assignable content a context can contain.
- [var customTypeName: String?](clscontext/customtypename.md)
  An optional name that the system presents to the user if you choose the custom context type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/type)*