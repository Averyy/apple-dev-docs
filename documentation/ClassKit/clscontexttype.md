# CLSContextType

**Framework**: ClassKit  
**Kind**: enum

The kinds of assignable content a context can contain.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum CLSContextType
```

#### Overview

When you initialize a new context with [`init(type:identifier:title:)`](clscontext/init(type:identifier:title:).md), you specify its [`type`](clscontext/type.md) to provide an indication of how your content is structured. The type doesn’t affect the context’s behavior, but it does provide an important indicator to teachers trying to understand your app’s content.

## Topics

### Context Types
- [CLSContextType.app](clscontexttype/app.md)
  An app context.
- [CLSContextType.audio](clscontexttype/audio.md)
  An audio context.
- [CLSContextType.book](clscontexttype/book.md)
  A book context.
- [CLSContextType.challenge](clscontexttype/challenge.md)
  A challenge context.
- [CLSContextType.chapter](clscontexttype/chapter.md)
  A chapter context.
- [CLSContextType.course](clscontexttype/course.md)
  A context that represents an entire course.
- [CLSContextType.custom](clscontexttype/custom.md)
  A context for assignable content that isn’t represented by one of the built-in context types.
- [CLSContextType.document](clscontexttype/document.md)
  A document context.
- [CLSContextType.exercise](clscontexttype/exercise.md)
  An exercise context.
- [CLSContextType.game](clscontexttype/game.md)
  A game context.
- [CLSContextType.lesson](clscontexttype/lesson.md)
  A lesson context.
- [CLSContextType.level](clscontexttype/level.md)
  A level context.
- [CLSContextType.none](clscontexttype/none.md)
  No type is assigned.
- [CLSContextType.page](clscontexttype/page.md)
  A page context.
- [CLSContextType.quiz](clscontexttype/quiz.md)
  A quiz context.
- [CLSContextType.section](clscontexttype/section.md)
  A section context.
- [CLSContextType.task](clscontexttype/task.md)
  A task context.
- [CLSContextType.video](clscontexttype/video.md)
  A video context.
### Initializers
- [init?(rawValue: Int)](clscontexttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var type: CLSContextType](clscontext/type.md)
  The kind of content a context represents.
- [func setType(CLSContextType)](clscontext/settype(_:).md)
  Updates the kind of content that a context represents.
- [var customTypeName: String?](clscontext/customtypename.md)
  An optional name that the system presents to the user if you choose the custom context type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontexttype)*