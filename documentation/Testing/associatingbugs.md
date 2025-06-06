# Associating bugs with tests

**Framework**: Swift Testing

Associate bugs uncovered or verified by tests.

#### Overview

Tests allow developers to prove that the code they write is working as expected. If code isn’t working correctly, bug trackers are often used to track the work necessary to fix the underlying problem. It’s often useful to associate specific bugs with tests that reproduce them or verify they are fixed.

> **Note**: “Bugs” as described in this document may also be referred to as “issues.” To avoid confusion with the [`Issue`](issue.md) type in the testing library, this document consistently refers to them as “bugs.”

“Bugs” as described in this document may also be referred to as “issues.” To avoid confusion with the [`Issue`](issue.md) type in the testing library, this document consistently refers to them as “bugs.”

#### Associate a Bug with a Test

To associate a bug with a test, use one of these functions:

- [`bug(_:_:)`](trait/bug(_:_:).md)
- [`bug(_:id:_:)`](trait/bug(_:id:_:)-10yf5.md)
- [`bug(_:id:_:)`](trait/bug(_:id:_:)-3vtpl.md)

The first argument to these functions is a URL representing the bug in its bug-tracking system:

```swift
@Test("Food truck engine works", .bug("https://www.example.com/issues/12345"))
func engineWorks() async {
  var foodTruck = FoodTruck()
  await foodTruck.engine.start()
  #expect(foodTruck.engine.isRunning)
}
```

You can also specify the bug’s  in its bug-tracking system in addition to, or instead of, its URL:

```swift
@Test(
  "Food truck engine works",
  .bug(id: "12345"),
  .bug("https://www.example.com/issues/67890", id: 67890)
)
func engineWorks() async {
  var foodTruck = FoodTruck()
  await foodTruck.engine.start()
  #expect(foodTruck.engine.isRunning)
}
```

A bug’s URL is passed as a string and must be parseable according to [`RFC 3986`](https://developer.apple.comhttps://www.ietf.org/rfc/rfc3986.txt). A bug’s unique identifier can be passed as an integer or as a string. For more information on the formats recognized by the testing library, see [`Interpreting bug identifiers`](bugidentifiers.md).

#### Add Titles to Associated Bugs

A bug’s unique identifier or URL may be insufficient to uniquely and clearly identify a bug associated with a test. Bug trackers universally provide a “title” field for bugs that is not visible to the testing library. To add a bug’s title to a test, include it after the bug’s unique identifier or URL:

```swift
@Test(
  "Food truck has napkins",
  .bug(id: "12345", "Forgot to buy more napkins")
)
func hasNapkins() async {
  ...
}
```

## See Also

- [Adding tags to tests](addingtags.md)
  Use tags to provide semantic information for organization, filtering, and customizing appearances.
- [Adding comments to tests](addingcomments.md)
  Add comments to provide useful information about tests.
- [Interpreting bug identifiers](bugidentifiers.md)
  Examine how the testing library interprets bug identifiers provided by developers.
- [macro Tag()](tag().md)
  Declare a tag that can be applied to a test function or test suite.
- [static func bug(String, Comment?) -> Self](trait/bug(_:_:).md)
  Constructs a bug to track with a test.
- [static func bug(String?, id: String, Comment?) -> Self](trait/bug(_:id:_:)-10yf5.md)
  Constructs a bug to track with a test.
- [static func bug(String?, id: some Numeric, Comment?) -> Self](trait/bug(_:id:_:)-3vtpl.md)
  Constructs a bug to track with a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/associatingbugs)*