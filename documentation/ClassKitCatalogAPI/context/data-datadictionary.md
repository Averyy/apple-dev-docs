# Context.Data

**Framework**: ClassKit Catalog API  
**Kind**: dictionary

The data that makes up a context.

**Availability**:
- ClassKit 1.0+

## Declaration

```swift
object Context.Data
```

## Mentions

- [Preparing Context Data](preparing-context-data.md)

#### Discussion

The description for each field includes a link to the equivalent property of the [`CLSContext`](https://developer.apple.com/documentation/ClassKit/CLSContext) class.

## Topics

### Progress Reporting
- [object Context.Data.ProgressReportingCapabilities](context/data-data.dictionary/progressreportingcapabilities-data.dictionary.md)
  The progress reporting capabilities supported by a context.

## Properties

- `customTypeName` (string): A name that the system presents to the user if you choose the custom context type. The API ignores this field if the `type` field is anything besides `custom`. For the equivalent property in your app, see [`customTypeName`](https://developer.apple.com/documentation/ClassKit/CLSContext/customTypeName).
- `displayOrder` (number): The position of a context relative to its siblings. For the equivalent property in your app, see [`displayOrder`](https://developer.apple.com/documentation/ClassKit/CLSContext/displayOrder).
- `identifierPath` ([string]) *(required)*: The identifier path, given as an array of strings, that locates the context within the data store’s context hierarchy. Each string in the array represents a context, starting from the main app context, through any ancestor contexts, down to the child context. For the equivalent property in your app, see [`identifierPath`](https://developer.apple.com/documentation/ClassKit/CLSContext/identifierPath). Like in your app, limit identifier paths to a maximum of eight entries, and 256 total characters. Unlike in your app, when communicating with the ClassKit Catalog API, you must explicitly specify the main app context as part of the identifier path.
- `isAssignable` (boolean): A Boolean that indicates whether teachers can assign the context as a task. For the equivalent property in your app, see [`isAssignable`](https://developer.apple.com/documentation/ClassKit/CLSContext/isAssignable).
- `progressReportingCapabilities` ([Context.Data.ProgressReportingCapabilities]): The kinds of progress reporting that the context can perform. For the equivalent property in your app, see [`progressReportingCapabilities`](https://developer.apple.com/documentation/ClassKit/CLSContext/progressReportingCapabilities). If you don’t include a `duration` capability when creating a context, the system adds one with an empty `details` field.
- `suggestedAge` ([number]): The range of ages, measured in years, for which you deem a context’s content suitable. For the equivalent property in your app, see [`suggestedAge`](https://developer.apple.com/documentation/ClassKit/CLSContext/suggestedAge). Format the age range as an array with two integers, the first of which indicates a lower bound (set to `0` to indicate no lower bound), and the second of which indicates an upper bound (set to the maximum value of `2^63-2` to indicate no upper bound). For example, for ages 4 to 6, set the value to `[4, 6]`. If you don’t set a value for this field, the system assumes suitability for all ages.
- `suggestedCompletionTime` ([number]): A suggested time range to complete a task, measured in minutes. For the equivalent property in your app, see [`suggestedCompletionTime`](https://developer.apple.com/documentation/ClassKit/CLSContext/suggestedCompletionTime). Format the completion time range as an array with two integers, the first of which indicates a lower bound (set to `0` to indicate no lower bound), and the second of which indicates an upper bound (set to the maximum value of `2^63-2` to indicate no upper bound). For example, for a completion time of 10 to 15 minutes, set the value to `[10, 15]`.
- `summary` (string): An optional, user-visible description of the context. For the equivalent property in your app, see [`summary`](https://developer.apple.com/documentation/ClassKit/CLSContext/summary).
- `thumbnailId` (string): An identifier for the thumbnail associated with the context. To access a thumbnail in your app, see [`thumbnail`](https://developer.apple.com/documentation/ClassKit/CLSContext/thumbnail). When creating a context, provide an identifier, and then use the same identifier when you upload the corresponding thumbnail image with a call to [`Create or Replace a Thumbnail`](create-or-replace-a-thumbnail.md).
- `title` (string) *(required)*: The name of the context as it appears to users, which must contain at least one non-whitespace character. For the equivalent property in your app, see [`title`](https://developer.apple.com/documentation/ClassKit/CLSContext/title).
- `topic` (string): The area of study to which a context relates. For the equivalent property in your app, see [`topic`](https://developer.apple.com/documentation/ClassKit/CLSContext/topic).
- `type` (string) *(required)*: The kind of content a context represents. For the equivalent property in your app, see [`type`](https://developer.apple.com/documentation/ClassKit/CLSContext/type).
- `universalLinkURL` (string): A URL that leads to the content in your app associated with the current context. For the equivalent property in your app, see [`universalLinkURL`](https://developer.apple.com/documentation/ClassKit/CLSContext/universalLinkURL).

## See Also

- [object Context.Metadata](context/metadata-data.dictionary.md)
  Information that helps the system categorize a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitcatalogapi/context/data-data.dictionary)*