# Orchestrating complex actions with app skills

**Framework**: App Intents  
**Role**: Article

Guide Siri AI through a complex task that involves several tool intents by providing an app skill.

## Overview

A tool intent performs a single action within your app, and Siri AI often performs only the one tool intent it needs to respond to a person’s request. When a person makes a complex request to perform a task, Siri might perform multiple tool intents and use several entities to fulfill that request. However, the information that individual tool intents and app entities provide can be insufficient for Siri to orchestrate them into more complex workflows.

> ❗ **Important**: The Siri AI Developer Preview is available in iOS, iPadOS, macOS, and visionOS on devices that support Apple Intelligence. During the preview, the App Intents API and Siri functionality may change.

To guide Siri AI through complex tasks that require several steps, create *app skills* that Xcode includes in your app to provide Siri with additional information it needs:

- How tool intents fit together to accomplish a task.
- Which tool intent to prefer when several intents could apply to a person’s request.
- What to avoid while performing a task.
- Domain knowledge specific to your app.
- Guidance Siri may use in a conversation flow for a series of tool intents, or for a tool intent with several parameters that may require clarification.

For example, an app skill for a shopping app might provide information to Siri AI about how to search items, add them to a shopping cart, choose payment and delivery methods, review the cart, and confirm the purchase.

> **Note**: You can’t use app skills to enforce deterministic behavior. Instead, app skills provide additional information that Siri AI uses to respond to complex requests. Siri AI doesn’t sequentially perform the tool intents that your skill lists.

## Add the skills bundle to your Xcode project

After creating the individual tool intents for a complex task, create the app skill that guides Siri AI through the complex task. To add skills to your app, start by adding a `Skills.skillsbundle` to your Xcode project. Your app can have several app skills, each of which is a Markdown file that you place within the bundle.

To add the skills bundle to your Xcode project:

1. Choose File > New > File from Template.
2. Select Skills Bundle in the Resource section, then click Next.
3. Keep the name `Skills` that Xcode suggests.
4. Select the app target in the Targets section, then create the bundle.

Xcode adds the `Skills.skillsbundle` with an empty `Skills` folder as a single item that you can expand in the Project navigator, and adds it to the target’s Copy Bundle Resources build phase.

> **Note**: An app target can only contain one `.skillsbundle`. If the bundle is missing from the app target’s Copy Bundle Resources phase or your skills bundle contains errors at compile time, your app doesn’t provide app skills to Siri.

## Create a skill file

The skill’s Markdown file contains the metadata and natural-language instructions that Siri needs to fulfill a complex request. At build time, Xcode validates the skills bundle and compiles it into your app bundle. On a device that supports the Siri AI Developer Preview, the system indexes the compiled skills of your app, its extensions, and its embedded frameworks.

For each app skill, add a subfolder to the `Skills` folder and name it after the skill, containing only lowercase letters, numbers, and hyphens. Then add a Markdown file to it that contains the skill. Each directory in `Skills/` represents one skill and must contain a `SKILL.md` file — don’t include other files in the skills bundle.

This example shows the structure of a skills bundle with two app skills:

```text
Skills.skillsbundle/
└── Skills/
    ├── name-of-skill-01/
    │   └── SKILL.md
    └── name-of-skill-02/
        └── SKILL.md
```

Skill names must be unique for your app, its extensions, and embedded frameworks. If two or more skills for your app use the same name, the system only uses one of them, which one is undefined.

The `SKILL.md` file consists of two main sections:

- High-level metadata that Siri AI uses to determine if the app skill matches a person’s request.
- A Markdown body with instructions and context that guide Siri through a complex request.

Siri reads the Markdown body only after it determines that the skill matches a request.

## Specify the skill’s metadata

When a person makes a request, Siri AI determines how to respond to the request. Siri considers the app skills you provide by reading the metadata you include at the top of the `SKILL.md` file.

Add the following at the top of your `SKILL.md` file, delimited by `---` lines, and include these fields to describe the app skill:

| Field | Possible values |
| --- | --- |
| `name` | The skill `name` is required and consists of 1-64 lowercase characters, including letters, digits, and hyphens; for example, `organize-files`. Don’t start or end the `name` with a hyphen, and don’t use double hyphens (`--`). The skill `name` must match the name of the skill’s directory. |
| `description` | The `description` is required, can’t be empty, must be a single line, and no longer than 1024 characters. It explains what the skill does and when to use it. Siri uses the description to decide whether the skill applies to a person’s request, without reading the body. |

This example shows the metadata for a skill that a travel planning app might provide to add a flight to a person’s itinerary:

```yaml
---
name: flight-add
description: This skill guides the user through adding a flight to TravelPlanningExample.
---
```

App skills use a subset of the [Agent Skills](https://agentskills.io/specification) format: the `name` and `description` frontmatter fields, and a Markdown body. Siri doesn’t support other frontmatter fields or supporting files like scripts or references.

## Provide guidance to Siri in the Markdown body

After the frontmatter, add the *body* to the `SKILL.md` file using Markdown syntax. It contains free-form instructions, limited to 10,000 characters, that Siri reads when it uses the app skill. The structure of the body is up to you. Consider these best practices:

- Siri is aware of your app intents and entities but may need additional guidance on which intent to use for a complex request, so your skill needs to provide that information. For example, tell Siri which intent to use for which step in a person’s complex request, the order to perform the app intents, how to disambiguate intents and entities, or what not to do.
- Siri uses the `title` and `description` attributes of your intents and entities to understand their purpose. Refer to intents, parameters, and entities informally, by what they do or represent. For example, include “call the get weather tool first” instead of “call GetWeatherIntent.”
- Don’t repeat what code already describes. This information is already in your app’s App Intents metadata, including titles and descriptions of intents, parameters, and entities.

The guidance you provide may include several paragraphs and headings, but it can be simple and consist of only one paragraph like this example from a flight tracking app:

```markdown
---
name: flight-add
description: Adds a flight with detailed information to the list of tracked flights.
---
When adding a flight using the create flight tool, be sure to
interview the user for the parameters if you don't already
have them. First, ask the user where they are going, and when
they leave. Then ask for the airline, then the flight number.
Finally, ask the user how long the flight is going to be and
calculate the end duration from there. When you've got all
the info, add the flight. Then, follow up with a prompt to
see if they want to name the flight, and give a suggested
name based on the info, or offer to let them change it. Lastly,
ask if the flight is for a friend or for them, and use the
set flight kind tool to update that information in
TravelPlanningExample.
```

## Verify your app skills

To manually verify your app skill, build and run your app on a device (not in the Simulator), or distribute it to internal testers with TestFlight. Bring the app to the foreground and try requests that each app skill’s `description` says it handles, or include the app name in requests while the app is in the background. Change the wording for a request to check that the description is specific enough for Siri AI to select the skill, and broad enough not to miss common phrases.

The Siri AI Developer Preview also lets you verify your app’s integration with Siri by creating specific evaluations you can run as part of your automated integration testing. For more information, see [Siri Evaluations](../sirievaluations/sirievaluations.md).

## See Also

### Getting started
- [Bringing custom actions and content to Siri](./bringing-custom-actions-and-content-to-siri.md)
  Support the Siri AI Developer Preview by turning custom app intents into tools Siri can call, and by helping Siri understand your app entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/orchestrating-complex-actions-with-app-skills)*