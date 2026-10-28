# Structured data models

**Framework**: Technology Overviews

Build a structured data model for your app, and persist that data model to disk or iCloud.

To manage even moderate amounts of data, you need an efficient system for storing and accessing it. You also need a system that’s easy to use and integrates with your app’s existing types. [SwiftData](../SwiftData/SwiftData.md) and [Core Data](../CoreData/CoreData.md) provide database-level features, without requiring an actual database. And when you do need a database to manage your content, [SQLite](https://sqlite.org/) is available on all Apple platforms.

## Build a structured model with modern Swift types

If you’re building your app using SwiftUI, [SwiftData](../SwiftData/SwiftData.md) makes a great companion for managing your data. With SwiftData, you can focus on building your app’s data structures first, and add persistence and other data management features second. That’s because SwiftData infers information about your data structures from the structures themselves. All you do is annotate your data structures with [information about how to manage them](https://developer.apple.com/videos/play/wwdc2023/10195).

SwiftData relies on Swift macros to inject code into your existing data structures. When you add the [`Model()`](../SwiftData/model%28%29.md) macro as shown in the example, SwiftData converts the structure into a stored model object and starts managing it. Additional macros tell SwiftData how to manage specific properties of your structure. For example, adding the `.unique` attribute to a property tells SwiftData to prevent the creation of multiple objects with the same value in that property.

```swift
import SwiftData

@Model
class Trip {
@Attribute(.unique) var name: String
var destination: String
var endDate: Date
var startDate: Date

@Relationship(.cascade) var bucketList: [BucketListItem]? = []
var livingAccomodation: LivingAccomodation?
}
```

You can use SwiftData to save your data to a local disk or to someone’s [iCloud account](../SwiftData/syncing-model-data-across-a-persons-devices.md). In your code, identify groups of objects you want to store together and put them into a [model container](../SwiftData/modelcontainer.md). Store all of your objects in one container or create multiple containers to manage different types of data separately. Retrieve objects from disk using a [query](../SwiftData/preserving-your-apps-model-data-across-launches.md). Because SwiftData works well with SwiftUI, you can incorporate queries directly into your app’s views and fetch your content there.

Like any modern data management system, SwiftData also supports the features that you need to ensure the integrity of your data. Add [concurrency support](../SwiftData/concurrencysupport.md) to your types to ensure fetch and save operations behave correctly in threaded code. The framework also provides built-in support for [undo operations](../SwiftData/reverting-data-changes-using-the-undo-manager.md), so people can revert unwanted changes.

---

## Build a structured model with any language

If you’re not using SwiftUI for your interface, or if you prefer to work in Objective-C, build your data model using [Core Data](../CoreData/CoreData.md). Core Data offers the same basic capabilities as SwiftData, including object-level management of data, query-based fetches, undo support, [iCloud support](../CoreData/mirroring-a-core-data-store-with-cloudkit.md), and more.

With Core Data, you build the schema for your data model visually using Xcode’s [model editor](../CoreData/modeling-data.md). Specify the entities for your data model and configure the attributes and relationships of those entities using this tool. At runtime, create [managed objects](../CoreData/nsmanagedobject.md) from the entities in your schema, put those objects in a [persistent container](../CoreData/core-data-stack.md) and save them to disk using a [managed object context](../CoreData/nsmanagedobjectcontext.md). Use the managed object context to coordinate other tasks, too, such as [undo operations](../CoreData/nsmanagedobjectcontext/undomanager.md).

## Store data using SQLite

If you’re already familiar with SQL databases, or simply need a lightweight and reliable database engine to manage large amounts of data, use [SQLite](https://sqlite.org/). This database engine is available in the SDK for all Apple platforms, so you can use the same code for all versions of your app. Use your code to store your app’s on-disk content, or to deliver content to your app over the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/structured-data-models)*