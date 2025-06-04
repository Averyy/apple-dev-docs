# Context7 Structure Recommendations for Apple Documentation

Based on Context7's documentation, here's how we should organize the Apple documentation for optimal integration:

## Directory Structure

```
apple-doc-scraper/
├── context7.json              # Context7 configuration
├── documentation/             # All documentation goes here
│   ├── README.md             # Overview of available frameworks
│   ├── swiftui/              # Framework folders (lowercase)
│   │   ├── README.md         # Framework overview & getting started
│   │   ├── text.md           # Individual API documentation
│   │   ├── button.md
│   │   ├── views/            # Group related APIs
│   │   │   ├── README.md     # Category overview
│   │   │   ├── vstack.md
│   │   │   └── hstack.md
│   │   └── modifiers/
│   │       ├── README.md
│   │       └── frame.md
│   ├── uikit/
│   ├── metal/
│   └── [framework]/
└── [other project files]
```

## Key Recommendations

### 1. Single Documentation Root
- Keep all documentation in the `documentation/` folder
- This makes the `folders` configuration simple: `["documentation"]`
- Context7 will index everything under this directory

### 2. Framework Organization
- Use lowercase folder names for consistency
- Each framework gets its own directory
- Add README.md in each framework folder with:
  - Framework overview
  - Common use cases
  - Getting started guide
  - Link to Apple's main framework page

### 3. API Grouping
For frameworks with many APIs, create logical subdirectories:
```
swiftui/
├── views/          # View types
├── modifiers/      # View modifiers
├── containers/     # Container views
├── controls/       # Interactive controls
└── data/          # Data flow APIs
```

### 4. File Naming Conventions
- Use lowercase with hyphens: `declaring-a-custom-view.md`
- For methods with parameters: `view_frame(width:height:alignment:).md`
- Keep names close to the actual API name for searchability

### 5. Metadata in Each File
Ensure each markdown file has:
```markdown
# [API Name]

**Framework**: [Framework]
**Category**: [Views/Modifiers/etc]
**Availability**: iOS 13.0+, macOS 10.15+

[Content...]
```

### 6. Cross-References
- Use relative links between related APIs
- Example: In `text.md`, link to `font.md` as `[font modifier](../modifiers/font.md)`
- This helps Context7 understand relationships

### 7. Rules for Better Context
Our `context7.json` includes rules that help with code generation:
- "Always specify the framework when referencing Apple APIs"
- "Include platform availability in code examples"
- "Use Swift syntax unless Objective-C is specifically requested"

### 8. Handling Scale
With 100,000+ pages across 150+ frameworks:
- Consider creating an index file per framework
- Use consistent categorization across frameworks
- Add framework-level README files for navigation

### 9. Search Optimization
To enable queries like "apple swiftui list":
- Include framework name in key locations
- Add common search terms in overview sections
- Use descriptive headings

### 10. Version Management
When Apple updates documentation:
- Use git tags for major documentation updates
- Update `previousVersions` in context7.json
- Consider keeping a CHANGELOG.md in documentation/

## Example Framework README

```markdown
# SwiftUI Documentation

SwiftUI is Apple's modern declarative framework for building user interfaces across all Apple platforms.

## Overview
SwiftUI provides views, controls, and layout structures for declaring your app's user interface.

## Common Topics
- [Text and Images](./text.md)
- [Stacks and Containers](./views/)
- [View Modifiers](./modifiers/)
- [State and Data Flow](./data/)

## Getting Started
```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        Text("Hello, World!")
    }
}
```

## Platform Requirements
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

---
*Source: [Apple Developer - SwiftUI](https://developer.apple.com/documentation/swiftui)*
```

## Benefits of This Structure

1. **Natural Language Queries**: "apple swiftui text" easily maps to `/documentation/swiftui/text.md`
2. **Scalable**: Can handle 150+ frameworks without confusion
3. **Maintainable**: Clear organization makes updates easier
4. **Context-Aware**: Framework grouping helps Context7 provide better suggestions
5. **User-Friendly**: Developers can browse documentation naturally