# Structured data models

**Framework**: Technology Overviews

Build a structured data model for your app, and persist that data model to disk or iCloud.

To manage even moderate amounts of data, you need an efficient system for storing and accessing it. You also need a system that’s easy to use and integrates with your app’s existing types. [`SwiftData`](https://developer.apple.com/documentation/SwiftData) and [`Core Data`](https://developer.apple.com/documentation/CoreData) provide database-level features, without requiring an actual database. And when you do need a database to manage your content, [`SQLite`](https://developer.apple.comhttps://sqlite.org/) is available on all Apple platforms.

#### Build a Structured Model with Modern Swift Types

If you’re building your app using SwiftUI, [`SwiftData`](https://developer.apple.com/documentation/SwiftData) makes a great companion for managing your data. With SwiftData, you can focus on building your app’s data structures first, and add persistence and other data management features second. That’s because SwiftData infers information about your data structures from the structures themselves. All you do is annotate your data structures with [`Model your schema with SwiftData`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10195).

You can use SwiftData to save your data to a local disk or to someone’s [`Syncing model data across a person’s devices`](https://developer.apple.com/documentation/SwiftData/Syncing-model-data-across-a-persons-devices). In your code, identify groups of objects you want to store together and put them into a [`ModelContainer`](https://developer.apple.com/documentation/SwiftData/ModelContainer). Store all of your objects in one container or create multiple containers to manage different types of data separately. Retrieve objects from disk using a [`Preserving your app’s model data across launches`](https://developer.apple.com/documentation/SwiftData/Preserving-your-apps-model-data-across-launches#Fetch-models-for-display-or-additional-processing). Because SwiftData works well with SwiftUI, you can incorporate queries directly into your app’s views and fetch your content there.

Like any modern data management system, SwiftData also supports the features that you need to ensure the integrity of your data. Add [`Concurrency support`](https://developer.apple.com/documentation/SwiftData/ConcurrencySupport) to your types to ensure fetch and save operations behave correctly in threaded code. The framework also provides built-in support for [`Reverting data changes using the undo manager`](https://developer.apple.com/documentation/SwiftData/Reverting-data-changes-using-the-undo-manager), so people can revert unwanted changes.

#### Build a Structured Model with Any Language

If you’re not using SwiftUI for your interface, or if you prefer to work in Objective-C, build your data model using [`Core Data`](https://developer.apple.com/documentation/CoreData). Core Data offers the same basic capabilities as SwiftData, including object-level management of data, query-based fetches, undo support, [`Mirroring a Core Data store with CloudKit`](https://developer.apple.com/documentation/CoreData/mirroring-a-core-data-store-with-cloudkit), and more.

With Core Data, you build the schema for your data model visually using Xcode’s [`Modeling data`](https://developer.apple.com/documentation/CoreData/modeling-data). Specify the entities for your data model and configure the attributes and relationships of those entities using this tool. At runtime, create [`NSManagedObject`](https://developer.apple.com/documentation/CoreData/NSManagedObject) from the entities in your schema, put those objects in a [`Core Data stack`](https://developer.apple.com/documentation/CoreData/core-data-stack) and save them to disk using a [`NSManagedObjectContext`](https://developer.apple.com/documentation/CoreData/NSManagedObjectContext). Use the managed object context to coordinate other tasks, too, such as [`undoManager`](https://developer.apple.com/documentation/CoreData/NSManagedObjectContext/undoManager).

#### Store Data Using Sqlite

If you’re already familiar with SQL databases, or simply need a lightweight and reliable database engine to manage large amounts of data, use [`SQLite`](https://developer.apple.comhttps://sqlite.org/). This database engine is available in the SDK for all Apple platforms, so you can use the same code for all versions of your app. Use your code to store your app’s on-disk content, or to deliver content to your app over the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/structured-data-models)*