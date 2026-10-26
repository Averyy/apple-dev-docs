---
url: "https://docs.swift.org/latest/documentation/swift-6-concurrency-migration-guide/migrationstrategy"
framework: "Swift-Org/Swift-6-Concurrency-Migration-Guide"
---

# Migration Strategy

**Framework**: Swift-Org/Swift-6-Concurrency-Migration-Guide

Get started migrating your project to the Swift 6 language mode.

Enabling complete concurrency checking in a module can yield many data-race safety issues reported by the compiler. Hundreds, possibly even thousands of warnings are not uncommon. When faced with a such a large number of problems, especially if you are just beginning to learn about Swift’s data isolation model, this can feel insurmountable.

**Don’t panic.**

Frequently, you’ll find yourself making substantial progress with just a few changes. And as you do, your mental model of how the Swift concurrency system works will develop just as rapidly.

> ❗ **Important**: This guidance should not be interpreted as a recommendation. You should feel confident about using other approaches.

#### Strategy

This document outlines a general strategy that could be a good starting point. There is no one single approach that will work for all projects.

The approach has three key steps:

- Select a module
- Enable stricter checking with Swift 5
- Address warnings

This process will be inherently *iterative*. Even a single change in one module can have a large impact on the state of the project as a whole.

#### Begin from the Outside

It can be easier to start with the outer-most root module in a project. This, by definition, is not a dependency of any other module. Changes here can only have local effects, making it possible to keep work contained.

Your changes do not *need* to be contained to the module, however. Dependencies under your control that have [unsafe global state](./commonproblems.md#Unsafe-Global-and-Static-Variables) or [trivially-`Sendable` types](./commonproblems.md#Implicitly-Sendable-Types) can be the root cause of many warnings across your project. These can often be the best things to focus on first.

#### Use the Swift 5 Language Mode

You could find it quite challenging to move a project from Swift 5 with no checking directly to the Swift 6 language mode. It is possible, instead, to incrementally enable more of the Swift 6 checking mechanisms while remaining in Swift 5 mode. This will surface issues only as warnings, keeping your build and tests functional as you progress.

To start, enable a single upcoming concurrency feature. This allows you to focus on one *specific type* of problem at a time.

| Proposal | Description | Feature Flag |
| --- | --- | --- |
| [SE-0401](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0401-remove-property-wrapper-isolation.md) | Remove Actor Isolation Inference caused by Property Wrappers | `DisableOutwardActorInference` |
| [SE-0412](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0412-strict-concurrency-for-global-variables.md) | Strict concurrency for global variables | `GlobalConcurrency` |
| [SE-0418](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0418-inferring-sendable-for-methods.md) | Inferring `Sendable` for methods and key path literals | `InferSendableFromCaptures` |

These can be enabled independently and in any order.

After you have addressed issues uncovered by upcoming feature flags, the next step is to [enable complete checking](./enabledataracesafety.md) for the module. This will turn on all of the compiler’s remaining data isolation checks.

#### Address Warnings

There is one guiding principle you should use as you investigate warnings: **express what is true now**. Resist the urge to refactor your code to address issues.

You will find it beneficial to minimize the amount of change necessary to get to a warning-free state with complete concurrency checking. After that is done, use any unsafe opt-outs you applied as an indication of follow-on refactoring opportunities to introduce a safer isolation mechanism.

> **Note**: To learn more about addressing common problems, see [Common Compiler Errors](./commonproblems.md).

#### Iteration

At first, you’ll likely be employing techniques to disable or workaround data isolation problems. Once you feel like you’ve reached the stopping point for a higher-level module, target one of its dependencies that has required a workaround.

You don’t have to eliminate all warnings to move on. Remember that sometimes very minor changes can have a significant impact. You can always return to a module once one of its dependencies has been updated.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/swift-6-concurrency-migration-guide/migrationstrategy)*